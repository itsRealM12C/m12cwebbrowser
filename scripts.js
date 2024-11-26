document.getElementById('go').addEventListener('click', () => {
    const url = document.getElementById('url').value;
    const display = document.getElementById('display');
    display.src = url.startsWith('http') ? url : `https://${url}`;
});

document.getElementById('back').addEventListener('click', () => {
    document.getElementById('display').contentWindow.history.back();
});

document.getElementById('forward').addEventListener('click', () => {
    document.getElementById('display').contentWindow.history.forward();
});
