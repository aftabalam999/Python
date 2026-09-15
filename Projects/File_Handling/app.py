import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Python File Manager", page_icon="📁", layout="centered")

st.title("📁 Python File Manager")
st.caption("Create, read, update and delete files — built with Python + Streamlit")

operation = st.sidebar.radio(
    "Choose an operation",
    ["Create", "Read", "Update", "Delete"],
)

st.sidebar.markdown("---")
st.sidebar.write("Files in current folder:")
files = [f.name for f in Path(".").iterdir() if f.is_file()]
if files:
    st.sidebar.write(", ".join(files))
else:
    st.sidebar.write("_no files yet_")


def createFile():
    st.subheader("Create a file")
    name = st.text_input("File name with extension", key="create_name")
    data = st.text_area("What do you want to write", key="create_data")
    if st.button("Create file"):
        try:
            if not name:
                st.warning("Enter a file name first.")
                return
            path = Path(name)
            if not path.exists():
                with open(path, 'w') as fs:
                    fs.write(data)
                st.success("Your file is created successfully")
            else:
                st.error("Error: file name already exists")
        except Exception as err:
            st.error(f"An error occured as {err}")


def readFile():
    st.subheader("Read a file")
    name = st.text_input("File name with extension", key="read_name")
    if st.button("Read file"):
        try:
            if not name:
                st.warning("Enter a file name first.")
                return
            path = Path(name)
            if path.exists():
                with open(path, 'r') as fs:
                    content = fs.read()
                st.code(content or "(empty file)")
            else:
                st.error("Error: file name does not exist")
        except Exception as err:
            st.error(f"An error occured as {err}")


def updateFile():
    st.subheader("Update a file")
    name = st.text_input("File name with extension", key="update_name")
    choice = st.radio("Operation", ["Rename", "Append", "Overwrite"], key="update_choice")

    if choice == "Rename":
        newName = st.text_input("New file name with extension", key="new_name")
        if st.button("Rename file"):
            try:
                path = Path(name)
                newPath = Path(newName)
                if not path.exists():
                    st.error("Error: file name does not exist")
                elif newPath.exists():
                    st.error("File name is already exists")
                else:
                    path.rename(newPath)
                    st.success("File renamed successfully")
            except Exception as err:
                st.error(f"An error occured as {err}")

    if choice == "Append":
        content = st.text_area("Write here what you want to append", key="append_data")
        if st.button("Append content"):
            try:
                path = Path(name)
                if not path.exists():
                    st.error("Error: file name does not exist")
                else:
                    with open(path, 'a') as fs:
                        fs.write(f"\n {content}")
                    st.success("Your content append successfully")
            except Exception as err:
                st.error(f"An error occured as {err}")

    if choice == "Overwrite":
        data = st.text_area("Write the text that you want to overwrite", key="overwrite_data")
        if st.button("Overwrite file"):
            try:
                path = Path(name)
                if not path.exists():
                    st.error("Error: file name does not exist")
                else:
                    with open(path, 'w') as fs:
                        fs.write(data)
                    st.success("Your content overwritten successfully")
            except Exception as err:
                st.error(f"An error occured as {err}")


def deleteFile():
    st.subheader("Delete a file")
    name = st.text_input("File name with extension", key="delete_name")
    if st.button("Delete file", type="primary"):
        try:
            if not name:
                st.warning("Enter a file name first.")
                return
            path = Path(name)
            if path.exists():
                path.unlink()
                st.success("File is deleted Successfully")
            else:
                st.error("Error: File does not exists")
        except Exception as err:
            st.error(f"Error: Some error occured {err}")


if operation == "Create":
    createFile()
elif operation == "Read":
    readFile()
elif operation == "Update":
    updateFile()
elif operation == "Delete":
    deleteFile()