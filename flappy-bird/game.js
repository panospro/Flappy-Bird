// Get the canvas and context
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// Set up the game variables
const player = new Player(canvas.width / 2, canvas.height / 2, 20, 0.65, 0);
let score = 0;
let isGameOver = false;
let frameCount = 0;
let hitGroundGameOver = 0;

// Create the obstacles
const obstacles = [];

// Set up the game loop
function gameLoop() {
  // Increase frameCount by 1 each frame
  frameCount++;

  // Clear the canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  
  // Update the player's position
  player.update();

  // Draw the player
  player.draw(ctx);

  // Generate a new pipe every 100 frames
  if (frameCount % 150 === 0) {
    const gap = 150;
    const minheight = 50;
    const maxheight = canvas.height - minheight - gap;
    const height1 = Math.floor(Math.random() * (maxheight - minheight + 1) + minheight);
    const height2 = canvas.height - height1 - gap;
    const pipe1 = new Pipe(canvas.width, height1, true);
    const pipe2 = new Pipe(canvas.width , height2, false);
    obstacles.push(pipe1);
    obstacles.push(pipe2);
  }

  // Draw the pipes
  for (let i = 0; i < obstacles.length; i++) {
    if (obstacles[i].x + obstacles[i].width < 0) {
      obstacles.splice(i, 1);
    }

    if (obstacles[i].x + obstacles[i].width < player.x - 10 && !obstacles[i].scored) {
      score += 0.5;
      obstacles[i].scored = true;
    }
    

    obstacles[i].x -= 2;
    obstacles[i].draw(ctx);
  
    if (obstacles[i].collidesWith(player)) {
      isGameOver = true;
    }
  }

  // Draw the score
  ctx.fillStyle = "#FFFFFF"; // set the fill style to white
  ctx.font = "30px Arial";
  ctx.fillText(`Score: ${score}`, 10, 50);

  // Check for game over
  if (player.y > canvas.height || isGameOver) {
    ctx.fillStyle = "#000000"; // set the fill style to black
    ctx.font = "60px Arial";
    ctx.fillText("Game Over", canvas.width / 2 - 150, canvas.height / 2);

    // Check if the player lost by hitting the ground
    hitGroundGameOver = 1;
    return;
  }

  // Call the game loop again on the next frame
  requestAnimationFrame(gameLoop);
}

// Handle player input with spacebar
document.addEventListener("keydown", function(event) {
  if (event.code === "Space" && !isGameOver && hitGroundGameOver != 1) {
    player.jump();
  } else {
    // Reset the game if the player clicks after game over
    hitGroundGameOver = 0;
    player.x = canvas.width / 2;
    player.y = canvas.height / 2 - 150;
    player.velocity = 0;
    obstacles.splice(0, obstacles.length);
    score = 0;
    isGameOver = false;
    requestAnimationFrame(gameLoop);
  }
});

// Handle player input with click
canvas.addEventListener("click", function() {
  if (!isGameOver && hitGroundGameOver != 1) {
    player.jump();
  } else {
    // Reset the game if the player clicks after game over
    hitGroundGameOver = 0;
    player.x = canvas.width / 2;
    player.y = canvas.height / 2 - 150;
    player.velocity = 0;
    obstacles.splice(0, obstacles.length);
    score = 0;
    isGameOver = false;
    requestAnimationFrame(gameLoop);
  }
});

// Start the game loop
gameLoop();