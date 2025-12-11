console.log("WS client loaded");

const proto = location.protocol === "https:" ? "wss://" : "ws://";
const wsUrl = proto + location.host + "/ws/nur";

window.ws = new WebSocket(wsUrl);

window.ws.onopen = () => console.log("WS connected");
window.ws.onmessage = (ev) => console.log("WS message:", ev.data);
window.ws.onclose = () => console.log("WS closed");
window.ws.onerror = (err) => console.error("WS error:", err);
