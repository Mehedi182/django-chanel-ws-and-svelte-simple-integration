<!-- <script>
  import { onMount } from "svelte";
  import { writable } from "svelte/store";
  import axios from "axios";

  // Store to hold the chat messages
  let messages = writable([]);

  // WebSocket connection
  let socket;

  // Function to send a message
  async function sendMessage(message) {
    const response = await axios.post("http://localhost:8000", {
      content: message,
    });

    if (response) {
      const data = await response.data;
      socket.send(JSON.stringify({ message }));
      console.log("Message sent:", data);
    } else {
      console.error("Failed to send message.");
    }
  }

  async function getMessages() {
    const response = await axios.get("http://localhost:8000");

    if (response) {
      console.log(response);
      const data = await response.data;
      messages.set(data);
    } else {
      console.error("Failed to retrieve messages.");
    }
  }

  // Function to handle incoming messages
  function handleIncomingMessage(event) {
    console.log(event);
    const data = JSON.parse(event.data);
    console.log("Received message:", data.message);
    if (data && data.message != undefined) {
      messages.update((prevMessages) => [...prevMessages, data.message]);
    }
  }

  // Function to establish WebSocket connection
  function setupWebSocketConnection() {
    socket = new WebSocket("ws://localhost:8000/ws/chat/");

    socket.onopen = function () {
      console.log("WebSocket connection established.");
    };

    socket.onmessage = handleIncomingMessage;

    socket.onclose = function () {
      console.log("WebSocket connection closed.");
    };
  }

  onMount(() => {
    setupWebSocketConnection();
    getMessages();
  });
  let messageList = [];
  messages.subscribe((val) => {
    messageList = val;
  });
  // Function to handle form submission
  function handleSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const input = form.querySelector("input[type='text']");
    const message = input.value.trim();

    if (message) {
      // Send the message
      sendMessage(message);
      // Clear the input field
      input.value = "test";
    }
  }
</script>

<main>
  <h1>Chat App</h1>

  <ul>
    {#each $messageList as message}
      <li>{message.content}</li>
    {/each}
  </ul>

  <form on:submit={handleSubmit}>
    <input type="text" placeholder="Enter a message" required />
    <button type="submit">Send</button>
  </form>
</main>

<style>
  /* Add your desired styles here */
</style> -->
<script>
	import { onMount } from "svelte";
	import { writable } from "svelte/store";
	import axios from "axios";
  
	// Store to hold the chat messages
	const messages = writable([]);
  
	// WebSocket connection
	let socket;
  
	// Function to handle incoming messages
	function handleIncomingMessage(event) {
	  const data = JSON.parse(event.data);
	  console.log("Received message:", data.message);
	  messages.update((prevMessages) => [...prevMessages, data.message]);
	}
  
	// Function to send a message
	async function sendMessage(event) {
	  event.preventDefault();
  
	  const messageInput = event.target.querySelector('input[name="message"]');
	  const message = messageInput.value;
  
	  if (message) {
		socket.send(JSON.stringify({ message }));
		messageInput.value = "";
	  }
	}
  
	// Function to establish WebSocket connection
	function setupWebSocketConnection() {
	  socket = new WebSocket("ws://localhost:8000/ws/chat/");
  
	  socket.onopen = function () {
		console.log("WebSocket connection established.");
	  };
  
	  socket.onmessage = handleIncomingMessage;
  
	  socket.onclose = function () {
		console.log("WebSocket connection closed.");
	  };
	}
  
	// Function to retrieve chat messages
	async function getMessages() {
    const response = await axios.get("http://localhost:8000");

    if (response) {
      console.log(response);
      const data = await response.data;
      messages.set(data);
    } else {
      console.error("Failed to retrieve messages.");
    }
  }
  
	onMount(() => {
	  setupWebSocketConnection();
	  getMessages();
	});
  
	const messageList = messages;
  
  </script>
  
  <h1>Chat App</h1>
  
  <div>
	{#each $messageList as message}
		{#if message.id}
		  <p>{message.content}</p>
		{:else}
			<p>{message}</p>
		{/if}

	{/each}
  </div>
  
  <form on:submit={sendMessage}>
	<input type="text" name="message" placeholder="Enter your message" />
	<button type="submit">Send</button>
  </form>
  