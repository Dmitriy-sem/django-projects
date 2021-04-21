import React, {useEffect, useState} from 'react'
import TodoItem from './components/TodoItem'
import Context from './Context'


function App() {
    const [todos, setTodo] = useState([])
	const [todoTitle, setTitle] = useState('')

	function getCookie(name) {
		let cookieValue = null;
		if (document.cookie && document.cookie !== '') {
			let cookies = document.cookie.split(';');
			for (let i = 0; i < cookies.length; i++) {
				let cookie = cookies[i].trim();
				if (cookie.substring(0, name.length + 1) === (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}

	const addTodo = e => {
		  if (e.key === 'Enter'){
              let newId
              try {
                newId = todos[todos.length - 1].pk + 1
              } catch(e){
                newId = 1
              }
              const newItem = {pk: newId, title: todoTitle, is_done: false}
			   fetch('http://127.0.0.1:8000/api/task-create/', {
			      method:'POST',
			      headers:{
			        'Content-type': 'application/json',
			        'X-CSRFToken': getCookie('csrftoken'),
			      },
			      body: JSON.stringify(newItem)
			    })
			  setTitle('')
			  setTodo([...todos, newItem])
		  }
	  }

	function removeTodo(id){
	    fetch(`http://127.0.0.1:8000/api/task-delete/${id}/`, {
	      method:'DELETE',
	      headers:{
	        'Content-type': 'application/json',
	        'X-CSRFToken': getCookie('csrftoken'),
	      },
	    })
		setTodo(todos.filter(item => item.pk !== id))
	}


	function toggleTodo(id){
		function findItem(){
			for (let i of todos){
				if (i.pk === id){
					return !i.is_done
				} 
			}
			return true
		}
		
		const editField = JSON.stringify({is_done: findItem()})
		
		fetch(`http://127.0.0.1:8000/api/task-update/${id}/`, {
	      method:'PATCH',
	      headers:{
	        'Content-type': 'application/json',
	        'X-CSRFToken': getCookie('csrftoken'),
	      },
		  body: editField
	    })

		setTodo(todos.map(item => {
			if (item.pk === id){
				item.is_done = !item.is_done
			}
			return item
		}))
	}

	useEffect(
		() => {
			fetch('http://127.0.0.1:8000/api/task-list/')
			  .then(response => response.json())
			  .then(data => setTodo(data))
			}, [])
	

    return (
      <Context.Provider value={{removeTodo, toggleTodo}}>
        <div className="container">
          <h1>Todo app</h1>
            <div className="input-field">
              <input type="text" value={todoTitle} onChange={(e) => setTitle(e.target.value)} onKeyPress={addTodo}/>
              <label>Todo name</label>
            </div>
			<ul>
				{todos.map(task => <TodoItem key={task.pk} todos={task} />)}
			</ul>
	        
        </div>
      </Context.Provider>
    );
}

export default App