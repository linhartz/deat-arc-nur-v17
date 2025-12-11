console.log("WS client loaded");

let ws = null;

function connectWS() {
    const proto = location.protocol === "https:" ? "wss://" : "ws://";
    const url = proto + location.host + "/ws";

    ws = new WebSocket(url);

    ws.onopen = () => console.log("WS connected");
    ws.onmessage = (ev) => console.log("WS message:", ev.data);
    ws.onclose = () => console.log("WS closed");
    ws.onerror = (err) => console.error("WS error:", err);
}

connectWS();
