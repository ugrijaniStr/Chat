const socket = io();
let username = "";

function getUsername() {
    const input = document.getElementById("username");
    if (input.value.trim() !== "") {
        username = input.value.trim();
        document.getElementById("popupArea").style.display = "none";
    }
}
window.getUsername = getUsername;

document.getElementById("message").addEventListener("keydown", function (e) {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        const msg = this.value.trim();
        if (msg !== "") {
            socket.emit("send_message", {
                user: username,
                message: msg
            });
            this.value = "";
        }
    }
});

socket.on("connect", () => {
    console.log("✅ SocketIO povezan!");
});

socket.on("receive_message", function (data) {
    const chat = document.getElementById("chatMessages");

    const chatChild = document.createElement("div");
    chatChild.classList.add("chatChild");

    const left = document.createElement("div");
    const right = document.createElement("div");

    const inner = document.createElement("div");

    const userDiv = document.createElement("div");
    userDiv.textContent = data.user;

    const messageDiv = document.createElement("div");
    messageDiv.textContent = data.message;

    inner.appendChild(userDiv);
    inner.appendChild(messageDiv);

    chatChild.appendChild(left);
    chatChild.appendChild(inner);
    chatChild.appendChild(right);

    chat.appendChild(chatChild);
    chat.scrollTop = chat.scrollHeight;
});
