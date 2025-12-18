import streamlit as st

st.title("To-Do List App")

# Initialize session state for tasks if not already done
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Input for new task
new_task = st.text_input("Add a new task:")
if st.button("Add Task") and new_task:
    st.session_state.tasks.append({"task": new_task, "done": False})
    st.success("Task added!")

# Display tasks
st.subheader("Your Tasks:")
for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([4, 1])
    with col1:
        if st.checkbox(task["task"], value=task["done"], key=f"task_{i}"):
            st.session_state.tasks[i]["done"] = True
        else:
            st.session_state.tasks[i]["done"] = False
    with col2:
        if st.button("Delete", key=f"delete_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()

# Clear all tasks
if st.button("Clear All"):
    st.session_state.tasks = []
    st.success("All tasks cleared!")