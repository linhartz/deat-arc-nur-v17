console.log("WS client loaded");

let ws = null;

function connectWS() {
    const proto = location.protocol === "https:" ? "wss://" : "ws://";
    const url = proto + location.host + "/ws/nur";
    ws = new WebSocket(url);

    ws.onopen = () => console.log("WS connected");
    ws.onmessage = (ev) => {
        console.log("WS message:", ev.data);
        try {
            const res = JSON.parse(ev.data);
            displayResult(res);
        } catch(e){
            console.error("Invalid WS response", e);
        }
    };
    ws.onclose = () => console.log("WS closed");
    ws.onerror = (err) => console.error("WS error:", err);
}

connectWS();
