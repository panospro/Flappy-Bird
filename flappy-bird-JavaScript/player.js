/* eslint-disable */
class Player {
  constructor(x, y, radius, gravity, velocity) {
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.gravity = gravity;
    this.velocity = velocity;
    this.image = new Image();
    this.image.src = "./images/bird.png";
    this.loaded = false;
    this.animationState = "up";
    this.animationStartTime = 0;
    this.image.onload = () => {
      this.loaded = true;
    };
  }

  // Draw the player as a bird
  draw(ctx) {
    if (this.loaded) {
      let angle = 0;
      if (this.animationState === "up") {
        angle = -45;
      } else if (this.animationState === "down") {
        angle = 90;
      }
      ctx.save();
      ctx.translate(this.x, this.y);
      ctx.rotate((Math.PI / 180) * angle);
      ctx.drawImage(
        this.image,
        -this.radius,
        -this.radius,
        this.radius * 2,
        this.radius * 2
      );
      ctx.restore();
    } else {
      const image = new Image();
      image.src = "./images/bird.png";
      ctx.drawImage(
        image,
        this.x - this.radius,
        this.y - this.radius,
        this.radius * 2,
        this.radius * 2
      );
    }
  }

  // Update the player's position based on gravity and velocity
  update() {
    this.velocity += this.gravity;
    this.y += this.velocity;
    if (this.velocity < 0) {
      // Player is going up
      this.animationState = "up";
    } else if (
      this.velocity >= 0 &&
      Date.now() - this.animationStartTime > 600
    ) {
      // Player has been falling for more than 1 second
      this.animationState = "down";
    }
  }

  // Make the player jump by giving it an upward velocity
  jump() {
    this.velocity = -10;
    this.animationState = "up";
    this.animationStartTime = Date.now();
  }

  // Check if the player has collided with an obstacle
  collidesWith(obstacle) {
    const dx = this.x - obstacle.x;
    const dy = this.y - obstacle.y;
    const distance = Math.sqrt(dx * dx + dy * dy);
    return distance < this.radius + obstacle.width / 2;
  }
}
