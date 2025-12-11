// ws-client.js
console.log("WS client loaded");

let ws = null;

function connectWS() {
    // vybere protokol podle stránky
    const proto = location.protocol === "https:" ? "wss://" : "ws://";
    const url = proto + location.host + "/ws/nur"; // odpovídá main.py

    ws = new WebSocket(url);

    ws.onopen = () => {
        console.log("WS connected");
    };

    ws.onmessage = (ev) => {
        console.log("WS message:", ev.data);
        // sem můžeme později přidat automatické zpracování zpráv
    };

    ws.onclose = () => console.log("WS closed");
    ws.onerror = (err) => console.error("WS error:", err);
}

// připojí se hned po načtení stránky
connectWS();

// --- volitelná funkce pro odesílání zpráv z editoru ---
function sendWSMessage(message) {
    if(ws && ws.readyState === WebSocket.OPEN){
        ws.send(message);
        console.log("WS sent:", message);
    } else {
        console.warn("WS not connected yet");
    }
}
