function setup() {
  // put setup code here
  createCanvas(1920, 980);
}

function draw() {
   //put drawing code here
   // fill(255, 255, 255);//kolor
   // strokeWeight(12);//grubość konturu
   // ellipse (150, 100, 80, 90);
   // ellipse (200, 100, 80, 90);
   // //oczy
   // fill(0, 0, 0);
   // ellipse (150, 100, 10, 10);
   // ellipse (200, 100, 10, 10);
   // //źrenice
   // noFill()
   // curve(130, 100, 100, 175, 250, 175, 100, 90);

   r = random(255);
   g = random(255);
   b = random(255);
   noFill();
   noStroke();

     if (mouseIsPressed) {
       if (mouseButton === LEFT) {

       strokeWeight(100);
       fill(r, g, b, 127);
       stroke(r, g, b);
     }
     if (mouseButton === CENTER) {
       strokeWeight(30);
       fill(255, 255, 255);
       stroke(255, 255, 255);
     }
   } else {
     noFill();
     noStroke();
}

   point(mouseX, mouseY);


   // if (mouseIsPressed) {
   //   if (mouseButton === LEFT) {
   //     elipse()
   //   } else {
   //     noFill();
   //     noStroke();
   //   }
   //   point(mouseX, mouseY);
   // }
 }
