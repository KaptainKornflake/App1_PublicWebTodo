import streamlit as st
import app1_functions
from app1_functions import write_todos

todos = app1_functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    app1_functions.write_todos(todos)




# 'st.camera_input(label="Camera Input")
st.title("This is the st.title function")
st.subheader("This uses the st.subheader function")
st.write("This uses the st.write function")

for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key = item)
    if checkbox:
        todos.pop(index)
        app1_functions.write_todos((todos))
        del st.session_state[item]
        st.rerun()

st.text_input(label= "Enter a todo: ",placeholder="This is a placeholder",
              on_change=add_todo,key="new_todo")

print("Hello")

st.session_state