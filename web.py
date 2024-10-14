import streamlit as st
import module

todos = module.todo_fun()


def add_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    module.write_todo(todos)


st.title("My Todo App")
st.subheader("This is my todo list app")
st.write("This app is to increase your work productivity")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        module.write_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")

