import turtle

class MyTurtle:
    def __init__ (self, color, shape):
        self.t = turtle.Turtle() #object dari class turtle
        self.t.color(color)  #mengatur warna turtle
        self.t.shape(shape) #mengatur bentuk turtle

    def maju(self, jarak):
        #method untuk menggerakkan
        self.t.forward(jarak)

    def putar_kiri(self, sudut):
        self.t.left(sudut)

    def buat_segitiga(self, ukuran):
        #method untuk membuat pesergi
        for _ in range(3):
            self.maju(ukuran)
            self.putar_kiri(120) #sudut 120 derajat untuk pesergi

    def selesai(self):
        #method untuk menyelesaikan turtle
        turtle.done()

#membuat objek turtle dengan warna dan bentuk
turtle1 = MyTurtle("red", "turtle")

#membuat pesergi dengan ukuran sisi 120
turtle1.buat_segitiga(120)

#menyelesaikan gambar
turtle1.selesai()


