document.addEventListener("DOMContentLoaded", function () {
    const chatForm = document.getElementById("chat-form");
    const messageInput = document.getElementById("message-input");
    const chatBox = document.getElementById("chat-box");
    const chatMode = document.getElementById("chat-mode");

    chatForm.addEventListener("submit", async function (event) {
        event.preventDefault();

        const userMessage = messageInput.value.trim();
        if (!userMessage) return;

        chatBox.innerHTML += `<div class="user-message">${userMessage}</div>`;

        messageInput.value = "";

        const formData = new FormData();
        formData.append("message", userMessage);
        formData.append("mode", chatMode.value);

        try {
            const response = await fetch("/api/chat", {
                method: "POST",
                body: formData
            });

            const data = await response.json();
            chatBox.innerHTML += `<div class="ai-message">${data.response}</div>`;
        } catch (error) {
            console.error("Error:", error);
        }
    });
});
