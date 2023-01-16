get = id => document.getElementById(id)
sleep = delay => new Promise((resolve) => setTimeout(resolve, delay))
async function started() {
    for (char of "Regi Weboldala".split("")) {
        get("h1").innerHTML += char;
        await sleep(100);
    }
}
function orarend() {
    get("fooldal").style.display = "none";
    get("orarend").style.display = "unset";
    get("muzsikák").style.display = "unset";
}
function fooldal() {
    get("orarend").style.display = "none";
    get("fooldal").style.display = "unset";
    get("muzsikák").style.display = "unset";
}
