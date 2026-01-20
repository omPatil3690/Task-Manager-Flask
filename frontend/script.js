const API_URL="http://localhost:5000/api/tasks";

async function fetchTasks() {
  const res = await fetch(API_URL);
  const tasks = await res.json();

  const list = document.getElementById("taskList");
  list.innerHTML = "";

  tasks.forEach(task => {
    const li = document.createElement("li");
    li.innerHTML = `
      <input type="checkbox" ${task.completed ? "checked" : ""} 
        onchange="toggleTask(${task.id}, this.checked)">
      ${task.title}
      <button onclick="deleteTask(${task.id})">X</button>
    `;
    list.appendChild(li);
  });
}


async function addTask() {
  const title = document.getElementById("taskInput").value;

  await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title })
  });

  document.getElementById("taskInput").value = "";
  fetchTasks();
}

async function toggleTask(id, completed) {
  await fetch(`${API_URL}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ completed })
  });
}

async function deleteTask(id) {
  await fetch(`${API_URL}/${id}`, {
    method: "DELETE"
  });
  fetchTasks();
}

fetchTasks();