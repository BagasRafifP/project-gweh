from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bagas | Personal Branding</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-slate-950 text-white">

  <!-- Hero Section -->
  <section class="min-h-screen flex flex-col justify-center items-center text-center px-6 bg-gradient-to-br from-slate-900 via-slate-950 to-slate-900">
    
    <img src="static/foto.jpg" 
         class="w-44 h-44 rounded-full border-4 border-sky-400 shadow-[0_0_40px_rgba(56,189,248,0.6)] hover:scale-105 transition duration-500 mb-6">

    <h1 class="text-5xl font-extrabold bg-gradient-to-r from-sky-400 to-cyan-300 text-transparent bg-clip-text">
      Bagas
    </h1>

    <p class="mt-4 text-slate-300 max-w-xl">
      Pelajar | Tech Enthusiast | Future Innovator  
      Membangun project kreatif dan eksplor teknologi setiap hari.
    </p>

    <a href="#about" 
       class="mt-8 px-8 py-3 bg-sky-400 text-black font-semibold rounded-full 
              hover:bg-cyan-300 hover:-translate-y-1 transition duration-300 shadow-lg">
      Kenal Lebih Dekat
    </a>
  </section>

  <!-- About -->
  <section id="about" class="py-24 px-6 bg-slate-900 text-center">
    <h2 class="text-3xl font-bold text-sky-400 mb-6">Tentang Saya</h2>
    <p class="max-w-2xl mx-auto text-slate-300 leading-relaxed">
      Saya pelajar yang tertarik dengan teknologi, Arduino, dan pengembangan kreatif.
      Suka membangun sesuatu dari nol dan memecahkan masalah dengan cara unik.
    </p>
  </section>

  <!-- Skills -->
  <section class="py-24 px-6 bg-slate-950 text-center">
    <h2 class="text-3xl font-bold text-sky-400 mb-12">Skill</h2>

    <div class="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
      <div class="bg-slate-900 p-8 rounded-2xl hover:bg-slate-800 transition shadow-xl">
        <h3 class="text-xl font-semibold mb-2">HTML & CSS</h3>
        <p class="text-slate-400 text-sm">Membangun UI clean & responsif</p>
      </div>

      <div class="bg-slate-900 p-8 rounded-2xl hover:bg-slate-800 transition shadow-xl">
        <h3 class="text-xl font-semibold mb-2">Arduino</h3>
        <p class="text-slate-400 text-sm">Hardware + coding project kreatif</p>
      </div>

      <div class="bg-slate-900 p-8 rounded-2xl hover:bg-slate-800 transition shadow-xl">
        <h3 class="text-xl font-semibold mb-2">Problem Solving</h3>
        <p class="text-slate-400 text-sm">Logika & analisis sistematis</p>
      </div>
    </div>
  </section>

  <!-- Contact -->
  <section class="py-24 px-6 bg-slate-900 text-center">
    <h2 class="text-3xl font-bold text-sky-400 mb-6">Kontak</h2>
    <p class="text-slate-300">Email: bagas@email.com</p>
    <p class="text-slate-300">Instagram: @bagas</p>
  </section>

  <footer class="py-6 text-center text-slate-500 text-sm bg-slate-950">
    © 2026 Bagas. All rights reserved :).
  </footer>

</body>
</html>'''