from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bagas | Tech Student</title>
<script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-slate-950 text-white scroll-smooth">

<!-- Navbar -->
<nav class="fixed top-0 w-full bg-slate-900/80 backdrop-blur z-50">
<div class="max-w-6xl mx-auto flex justify-between items-center p-4">
<h1 class="text-sky-400 font-bold text-xl">Bagas.dev</h1>

<div class="space-x-6 text-sm">
<a href="#about" class="hover:text-sky-400">About</a>
<a href="#skills" class="hover:text-sky-400">Skills</a>
<a href="#projects" class="hover:text-sky-400">Projects</a>
<a href="#contact" class="hover:text-sky-400">Contact</a>
</div>
</div>
</nav>


<!-- Hero -->
<section class="min-h-screen flex flex-col justify-center items-center text-center px-6">

<img src="static/Bagas.jpg"
class="w-44 h-44 rounded-full border-4 border-sky-400 shadow-[0_0_40px_rgba(56,189,248,0.6)] mb-6">

<h1 class="text-5xl font-bold text-sky-400">Bagas</h1>

<p class="mt-4 text-slate-300 max-w-xl">
Pelajar yang suka teknologi, Arduino, dan bikin project aneh tapi keren.
</p>

<div class="mt-8 flex gap-4">

<a href="#projects"
class="px-6 py-3 bg-sky-400 text-black rounded-full hover:bg-cyan-300 transition">
Lihat Project
</a>

<a href="https://instagram.com"
target="_blank"
class="px-6 py-3 border border-sky-400 rounded-full hover:bg-sky-400 hover:text-black transition">
Instagram
</a>

</div>

</section>


<!-- About -->
<section id="about" class="py-24 px-6 text-center bg-slate-900">

<h2 class="text-3xl font-bold text-sky-400 mb-6">Tentang Saya</h2>

<p class="max-w-2xl mx-auto text-slate-300">
Saya pelajar yang suka eksperimen teknologi seperti Arduino,
web development, dan berbagai project kreatif lainnya.
</p>

</section>


<!-- Skills -->
<section id="skills" class="py-24 px-6 text-center">

<h2 class="text-3xl font-bold text-sky-400 mb-12">Skill</h2>

<div class="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">

<div class="bg-slate-900 p-8 rounded-xl hover:bg-slate-800 transition">
<h3 class="text-xl font-semibold">HTML & CSS</h3>
<p class="text-slate-400 text-sm">UI modern dan responsif</p>
</div>

<div class="bg-slate-900 p-8 rounded-xl hover:bg-slate-800 transition">
<h3 class="text-xl font-semibold">Arduino</h3>
<p class="text-slate-400 text-sm">Hardware + coding</p>
</div>

<div class="bg-slate-900 p-8 rounded-xl hover:bg-slate-800 transition">
<h3 class="text-xl font-semibold">Python</h3>
<p class="text-slate-400 text-sm">Automation & backend</p>
</div>

</div>

</section>


<!-- Projects -->
<section id="projects" class="py-24 px-6 bg-slate-900 text-center">

<h2 class="text-3xl font-bold text-sky-400 mb-12">Project</h2>

<div class="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">

<div class="bg-slate-800 p-6 rounded-xl hover:scale-105 transition">
<h3 class="text-lg font-bold">Arduino LCD System</h3>
<p class="text-sm text-slate-400 mt-2">
Project LCD running text dengan tombol kontrol.
</p>

<button class="mt-4 px-4 py-2 bg-sky-400 text-black rounded">
Detail
</button>
</div>

<div class="bg-slate-800 p-6 rounded-xl hover:scale-105 transition">
<h3 class="text-lg font-bold">Python Web Server</h3>
<p class="text-sm text-slate-400 mt-2">
Web sederhana menggunakan Flask.
</p>

<button class="mt-4 px-4 py-2 bg-sky-400 text-black rounded">
Detail
</button>
</div>

<div class="bg-slate-800 p-6 rounded-xl hover:scale-105 transition">
<h3 class="text-lg font-bold">Game Prototype</h3>
<p class="text-sm text-slate-400 mt-2">
Eksperimen membuat game kecil.
</p>

<button class="mt-4 px-4 py-2 bg-sky-400 text-black rounded">
Detail
</button>
</div>

</div>

</section>


<!-- Contact -->
<section id="contact" class="py-24 px-6 text-center">

<h2 class="text-3xl font-bold text-sky-400 mb-6">Kontak</h2>

<div class="flex justify-center gap-6">

<a href="mailto:bagasrp1098@email.com"
class="px-6 py-3 bg-sky-400 text-black rounded-full">
Email
</a>

<a href="https://www.instagram.com/bagas_rafif_pratama/"
target="_blank"
class="px-6 py-3 border border-sky-400 rounded-full hover:bg-sky-400 hover:text-black">
Instagram
</a>

<a href="#"
class="px-6 py-3 border border-sky-400 rounded-full hover:bg-sky-400 hover:text-black">
GitHub
</a>

</div>

</section>


<footer class="py-6 text-center text-slate-500 text-sm">
© 2026 Bagas
</footer>

</body>
</html>
'''

app.run(host="0.0.0.0", port=5000)