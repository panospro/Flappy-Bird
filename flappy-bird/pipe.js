class Pipe {
    constructor(x, height, isTopPipe) {
        this.x = x;
        this.y = isTopPipe ? 0 : canvas.height - height;
        this.width = 80;
        this.height = height;

        this.image = new Image();
        this.image.src = isTopPipe ? "./images/fullPipeTop.png" : "./images/fullPipeBottom.png";
    }
    
    draw(ctx) {
        ctx.drawImage(this.image, this.x, this.y, this.width, this.height);
      }   
    
    collidesWith(player) {
      if (player.x < this.x || player.x > this.x + this.width) return false;
      if (player.y < this.y || player.y > this.y + this.height) return false;
      return true;
    }
}