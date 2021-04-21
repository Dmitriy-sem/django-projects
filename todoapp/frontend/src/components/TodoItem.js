import React, {useContext} from 'react'
import Context from '../Context'

function TodoItem(props) {
    const {pk, title, is_done} = props.todos
    const {removeTodo, toggleTodo} = useContext(Context)
    let clazz = 'todo'
    if (is_done){
        clazz += ' is_done'
    }

    return (
        <li className={clazz}>
        <label>
            <input type="checkbox" checked={is_done} onChange={() => toggleTodo(pk)}/>
            <span>{title}</span>
            <i className="fas fa-trash" onClick={() => removeTodo(pk)}/>
        </label>
        </li>
    )
}

export default TodoItem