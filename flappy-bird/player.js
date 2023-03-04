class Player {
  constructor(x, y, radius, gravity, velocity) {
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.gravity = gravity;
    this.velocity = velocity;

    this.image = new Image();
    this.image.src = "path/to/player_image.png";
    this.image.onload = () => {
      this.loaded = true;
    };
  }

  // Draw the player as a circle
  // draw(ctx) {
  //   ctx.beginPath();
  //   ctx.arc(this.x, this.y, this.radius, 0, 2 * Math.PI);
  //   ctx.fillStyle = "#000000";
  //   ctx.fill();
  // }

  draw(ctx) {
    if (this.loaded) {
      ctx.drawImage(this.image, this.x - this.radius, this.y - this.radius, this.radius * 2, this.radius * 2);
    }
    else {
    const image = new Image();
    image.src = "./images/bird.png";
    ctx.drawImage(image, this.x - this.radius, this.y - this.radius, this.radius * 2, this.radius * 2);
    }
  }

  
  // Update the player's position based on gravity and velocity
  update() {
    this.velocity += this.gravity;
    this.y += this.velocity;
  }

  // Make the player jump by giving it an upward velocity
  jump() {
    this.velocity = -10;
  }

  // Check if the player has collided with an obstacle
  collidesWith(obstacle) {
    const dx = this.x - obstacle.x;
    const dy = this.y - obstacle.y;
    const distance = Math.sqrt(dx * dx + dy * dy);
    return distance < this.radius + obstacle.width / 2;
  }
}
