// Get the canvas and context
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// Set up the game variables
const player = new Player(canvas.width / 2, canvas.height / 2, 20, 0.65, 0);
const obstacles = [];
let score = 0;
let isGameOver = false;

// Set up the game loop
function gameLoop() {
  // Clear the canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Update the player's position
  player.update();

  // Draw the player
  player.draw(ctx);

  // Move and draw the obstacles
  for (let i = 0; i < obstacles.length; i++) {
    const obstacle = obstacles[i];
    obstacle.x -= 5;
    ctx.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);

    // Check for collision with player
    if (player.collidesWith(obstacle)) {
      isGameOver = true;
    }

    // Remove obstacles that have gone off the screen
    if (obstacle.x + obstacle.width < 0) {
      obstacles.splice(i, 1);
      i--;
      score++;
    }
  }

  // Draw the score
  ctx.font = "30px Arial";
  ctx.fillText(`Score: ${score}`, 10, 50);

  // Check for game over
  if (player.y > canvas.height || isGameOver) {
    ctx.font = "60px Arial";
    ctx.fillText("Game Over", canvas.width / 2 - 150, canvas.height / 2);
    return;
  }

  // Call the game loop again on the next frame
  requestAnimationFrame(gameLoop);
}

// Handle player input
canvas.addEventListener("click", function() {
  if (!isGameOver) {
    player.jump();
  } else {
    // Reset the game if the player clicks after game over
    player.x = canvas.width / 2;
    player.y = canvas.height / 2;
    player.velocity = obstacles.splice(0, obstacles.length);
    score = 0;
    isGameOver = false;
    requestAnimationFrame(gameLoop);
    
  }
});

// Start the game loop
gameLoop();