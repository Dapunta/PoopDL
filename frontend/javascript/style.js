// Version
const version = 'Versi 1.5';
document.getElementById('app-version').innerText = version;

// Open Information Menu
document.getElementById('information-button-open').addEventListener('click', () => {
    document.getElementById('information-container').className = 'container-overlay-active poppins';
    document.querySelector('.full-container').style.overflowY = 'hidden';
});

// Close Information Menu
document.getElementById('information-button-close').addEventListener('click', () => {
    document.getElementById('information-container').className = 'container-overlay-inactive poppins';
    document.querySelector('.full-container').style.overflowY = 'auto';
});

// Loading Spinner 1
function loading(element_id, active) {
    const loadingBox = document.getElementById(element_id);
    if (active)  {
        loadingBox.innerHTML = `<div id="loading-spinner" class="spinner-container"><div class="spinner"></div></div>`;
        loadingBox.style.pointerEvents = 'all';
    }
    else {
        loadingBox.innerHTML = `Fetch`;
        loadingBox.style.pointerEvents = 'all';
    }
}

// Loading Spinner 2
function loading2(element_id, active) {
    const loadingBox = document.getElementById(element_id);
    if (active)  {
        loadingBox.innerHTML = `<div id="loading-spinner" class="spinner-container"><div class="spinner2"></div></div>`;
        loadingBox.style.pointerEvents = 'all';
    }
    else {
        loadingBox.innerHTML = `Failed`;
        loadingBox.style.pointerEvents = 'all';
    }
}

// Loading Spinner 3
function loading3(element_id, active) {
    const loadingBox = document.getElementById(element_id);
    if (active)  {
        loadingBox.innerHTML = `<div id="loading-spinner" class="spinner-container"><div class="spinner2"></div></div>`;
        loadingBox.style.pointerEvents = 'none';
    }
    else {
        loadingBox.innerHTML = `<i class="fa-solid fa-play"></i>`;
        loadingBox.style.pointerEvents = 'auto';
    }
}

// Time Sleep
function sleep(s) {
    return new Promise(resolve => setTimeout(resolve, s*1000));
}

// Add Information

const list_qna = [
    {'question':'Apa itu PoopDL?', 'answer':'PoopDL adalah platform untuk streaming atau mengunduh file PoopHD secara gratis dan cepat'},
    {'question':'Bagaimana cara menggunakannya?', 'answer':'Cukup masukkan URL PoopHD yang ingin kamu download, tekan submit, tunggu hingga muncul daftar file, kemudian pilih opsi Download atau Play Streaming'},
    {'question':'Apakah platform ini resmi?', 'answer':'Platform ini dibuat secara mandiri dan tidak memiliki asosiasi dengan PoopHD. Segala tindakan adalah tanggung jawab pengguna'},
];

function addInfo() {
    const box_info = document.getElementById('container-qna');
    list_qna.forEach((item) => {
        const new_element = document.createElement('div');
        new_element.className = 'box-qna';
        new_element.innerHTML = `
            <span class="question">${item.question}</span>
            <span class="answer">${item.answer}</span>`;
        box_info.appendChild(new_element);
    });
}

addInfo();

// Add Contact

const list_contact = [
    {'href':'https://www.facebook.com/Dapunta.Khurayra.X', 'icon':'<i class="fa-brands fa-square-facebook"></i>', 'text':'Dapunta Khurayra X'},
    {'href':'https://www.instagram.com/dapunta.ratya/#', 'icon':'<i class="fa-brands fa-square-instagram"></i>', 'text':'Dapunta Ratya'},
    {'href':'https://github.com/dapunta', 'icon':'<i class="fa-brands fa-square-github"></i>', 'text':'Dapunta'},
];

function AddContact() {
    const box_contact = document.getElementById('container-contact');
    list_contact.forEach((item) => {
        const new_element = document.createElement('a');
        Object.assign(new_element, { href: item.href, target: '_blank', rel: 'noopener' });
        new_element.innerHTML = `${item.icon}<span>${item.text}</span>`;
        box_contact.appendChild(new_element);
    });
}

AddContact();

// Zoom Image

function zoom(element) {
    const overlay_zoom = document.getElementById('zoom-container');
    overlay_zoom.className = 'container-zoom-active poppins';
    overlay_zoom.innerHTML = `<img src="${element.src}">`;
}

function unzoom(element) {
    const overlay_zoom = document.getElementById('zoom-container');
    overlay_zoom.innerHTML = '';
    overlay_zoom.className = 'container-zoom-inactive poppins';
}

// Error Fetch
function errorFetch() {
    const box_result = document.getElementById('result');
    box_result.innerHTML = `
        <div class="container-failed">
            <span>Fetch Failed</span>
        </div>`;
}