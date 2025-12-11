console.log("WS client loaded");

let ws = null;

function connectWS() {
    const proto = location.protocol === "https:" ? "wss://" : "ws://";
    const url = proto + location.host + "/ws/nur";  // musí sedět s main.py
    ws = new WebSocket(url);

    ws.onopen = () => console.log("WS connected");
    ws.onmessage = (ev) => {
        console.log("WS message:", ev.data);
        try {
            const res = JSON.parse(ev.data);
            displayResult(res); // nová funkce pro zobrazení ve stránce
        } catch(e) {
            console.error("Invalid WS response", e);
        }
    };
    ws.onclose = () => console.log("WS closed");
    ws.onerror = (err) => console.error("WS error:", err);
}

connectWS();

// Odesílání payloadu přes WS
function sendPayloadWS(payload, module, version) {
    if(ws && ws.readyState === WebSocket.OPEN){
        const message = JSON.stringify({ module, version, payload });
        ws.send(message);
    } else {
        alert("WebSocket není připojen.");
    }
}

// Funkce pro zobrazení výsledku ve stránce (tabulka)
function displayResult(result){
    let row = document.querySelector("#respTable tbody").insertRow(-1);
    row.insertCell(0).innerText = result.module || "";
    row.insertCell(1).innerText = result.version || "";
    row.insertCell(2).innerHTML = "<pre>"+JSON.stringify(result.payload,null,2)+"</pre>";

    const numericValue = Object.values(result.out)[0];
    const outCell = row.insertCell(3);
    outCell.innerHTML = "<pre>"+JSON.stringify(result.out,null,2)+"</pre>";
    outCell.className = numericValue>0.7?"green":(numericValue>0.4?"orange":"red");

    row.insertCell(4).innerText = result.comment || "";
}
