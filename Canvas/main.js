var DrawingApp = /** @class */ (function () {
    function DrawingApp(canvas) {
        var _this = this;
        this.circles = [];
        this.colors = ["red", "green", "blue"];
        this.colorsCount = 0;
        this.gravity = 0.5;
        this.friction = 0.8;
        this.redraw = function () {
            _this.context.fillStyle = "white";
            _this.context.fillRect(0, 0, _this.canvas.width, _this.canvas.height);
            for (var _i = 0, _a = _this.circles; _i < _a.length; _i++) {
                var circle = _a[_i];
                _this.drawCircle(circle);
                _this.moveCircle(circle);
            }
            requestAnimationFrame(_this.redraw);
        };
        this.addCircles = function (numbers) {
            var color = _this.getColor();
            for (var i = 0; i < numbers; i++) {
                _this.circles.push({
                    x: _this.canvas.width * Math.random(),
                    y: _this.canvas.height * Math.random(),
                    radius: 32 * Math.random() + 8,
                    xInc: 5 * Math.random() + 1,
                    yInc: 5 * Math.random() + 1,
                    color: color
                });
            }
        };
        this.canvas = canvas;
        this.context = canvas.getContext("2d");
        this.addCircles(10);
        requestAnimationFrame(this.redraw);
    }
    DrawingApp.prototype.drawCircle = function (circle) {
        this.context.fillStyle = circle.color;
        this.context.beginPath();
        this.context.arc(circle.x, circle.y, circle.radius, 0, 2 * Math.PI);
        this.context.fill();
    };
    DrawingApp.prototype.getColor = function () {
        var result = this.colors[this.colorsCount];
        this.colorsCount = (this.colorsCount + 1) % this.colors.length;
        return result;
    };
    DrawingApp.prototype.moveCircle = function (circle) {
        if (circle.x + circle.radius > this.canvas.width || circle.x - circle.radius <= 0) {
            circle.xInc *= -this.friction;
        }
        if (circle.y + circle.radius + circle.yInc > this.canvas.height) {
            circle.yInc *= -this.friction;
            circle.xInc *= this.friction;
        }
        else {
            circle.yInc += this.gravity;
        }
        circle.x += circle.xInc;
        circle.y += circle.yInc;
    };
    return DrawingApp;
}());
//# sourceMappingURL=main.js.map