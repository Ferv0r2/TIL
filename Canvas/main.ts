type Circle = {
    x: number,
    y: number,
    readonly radius: number,
    readonly color: string,
    xInc: number,
    yInc: number,
};

class DrawingApp {
    private canvas: HTMLCanvasElement;
    private context: CanvasRenderingContext2D;

    private readonly circles: Circle[] = [];
    private readonly colors: readonly string[] = ["red", "green", "blue"];
    
    private colorsCount: number = 0;

    private gravity: number = 0.5;
    private friction: number = 0.8;

    constructor(canvas: HTMLCanvasElement) {
        this.canvas = canvas;
        this.context = canvas.getContext("2d");
        

        this.addCircles(10);

        requestAnimationFrame(this.redraw);
    }

    private redraw = () => {
        this.context.fillStyle = "white";
        this.context.fillRect(0, 0, this.canvas.width, this.canvas.height);

        for (const circle of this.circles) {
            this.drawCircle(circle);
            this.moveCircle(circle);
        }

        requestAnimationFrame(this.redraw);
    }

    private drawCircle(circle: Circle) {
        this.context.fillStyle = circle.color;
        this.context.beginPath();
        this.context.arc(circle.x, circle.y, circle.radius, 0, 2 * Math.PI);
        this.context.fill();
    }

    private getColor(): string {
        let result = this.colors[this.colorsCount];
        this.colorsCount = (this.colorsCount + 1) % this.colors.length;
        return result;
    }

    private moveCircle(circle: Circle) {        
        if (circle.x + circle.radius > this.canvas.width || circle.x - circle.radius <= 0) {
            circle.xInc *= -this.friction;
        }

        if (circle.y + circle.radius + circle.yInc > this.canvas.height) {
            circle.yInc *= -this.friction;
            circle.xInc *= this.friction;
        } else {
            circle.yInc += this.gravity;
        }
        
        circle.x += circle.xInc;
        circle.y += circle.yInc;
    }

    public addCircles = (numbers: number) => {
        var color = this.getColor();
        for (var i = 0; i < numbers; i++) {
            this.circles.push({
                x: this.canvas.width * Math.random(),
                y: this.canvas.height * Math.random(),
                radius: 32 * Math.random() + 8,
                xInc: 5 * Math.random() + 1,
                yInc: 5 * Math.random() + 1,
                color: color
            });
        }
    }
}
