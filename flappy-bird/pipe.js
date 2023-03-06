// Implementation of the class Pipe
class Pipe {
    constructor(x, height, isTopPipe) {
        this.x = x;
        // If its a top-to-bottom pipe y will be set to 0, else to canvas.height-height 
        this.y = isTopPipe ? 0 : canvas.height - height; 
        this.width = 80;
        this.height = height;

        // Preload the image for faster refresh
        this.image = new Image();
        this.image.src = isTopPipe ? "./images/fullPipeTop.png" : "./images/fullPipeBottom.png";
    }
    
    // The draw function of pipes
    draw(ctx) {
        ctx.drawImage(this.image, this.x, this.y, this.width, this.height);
      }   
    
    // Function that checks if the player collided with the pipes
    collidesWith(player) {
      if (player.x < this.x || player.x > this.x + this.width) return false;
      if (player.y < this.y || player.y > this.y + this.height) return false;
      return true;
    }
}