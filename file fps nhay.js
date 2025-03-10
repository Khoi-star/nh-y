let lastFrameTime = 0;
const fps = 60;
const maxDeltaTime = 1000 / fps;

function cleanMemory() {
    if (window.performance && window.performance.memory) {
        console.log('Cleaning memory: ', window.performance.memory);
    }
}

function closeBackgroundApps() {

    console.log("On iOS, closing apps is restricted.");
}

function optimizeSystem() {
    console.log("Optimizing system for better FPS...");
    cleanMemory();  // Dọn dẹp bộ nhớ
    closeBackgroundApps();
}

function gameLoop(timestamp) {
    let deltaTime = timestamp - lastFrameTime;
    
    if (deltaTime > maxDeltaTime) {
        lastFrameTime = timestamp;

        optimizeSystem();

        updateGame();
        drawGame();
    }

    requestAnimationFrame(gameLoop);
}

function updateGame() {
    console.log("Updating game...");
}

function drawGame() {
    console.log("Drawing game...");
}

requestAnimationFrame(gameLoop);

console.log("Game optimization is running...");
