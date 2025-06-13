// Global
// const api = 'http://127.0.0.1:5000'; // Change This
const api = 'https://poopdl-api.dapuntaratya.com'; // Change This

// Global variable
let final_result = {
    "status"  : "failed",
    "message" : "gatau bjir",
    "data"    : []
};

// Add Event Listener Submit Button
const inputForm = document.getElementById('poop_url');
const submitButton = document.getElementById('submit_button');
submitButton.addEventListener('click', (event) => {
    const url = inputForm.value;
    readInput(url);
});

// Filter URL biar valid
function sanitizeUrl(url) {
    if (Array.isArray(url)) {
        return url
            .map(item => item.trim().replace(/ /g, '%20'))
            .filter(item => item !== '');
    } else if (typeof url === 'string') {
        const cleaned = url.trim().replace(/ /g, '%20');
        return cleaned === '' ? null : cleaned;
    } else {
        throw new Error('Invalid url format');
    }
}

// Read Input
async function readInput(raw_url) {

    const list_url = raw_url.replace(/\n/g, "").replace(/\s/g, '') === '' ? null : raw_url.split("\n");;

    if (list_url) {

        const stream_box = document.getElementById(`stream-video`);
        stream_box.innerHTML = '';
        stream_box.className = 'stream-video-section inactive'

        document.getElementById('result').innerHTML = '';
        loading('submit_button', true);

        const clean_url = sanitizeUrl(list_url);
        await fetchURL(clean_url);

        loading('submit_button', false);
        inputForm.value = '';
    }

    else {
        loading('submit_button', false);
        inputForm.value = '';
    }

    if (final_result.data.length == 0) {
        errorFetch();
    }

}

// Fetch URL
async function fetchURL(list_url) {

    try {

        const get_file_url = `${api}/get_file`;
        const headers = {'Content-Type':'application/json'};
        const payload = {url:list_url};

        const response = await fetch(get_file_url, {
            method: 'POST',
            mode: 'cors',
            headers: headers,
            body: JSON.stringify(payload)
        });
        const result = await response.json();
        final_result = result;

        if (result.status == 'success') {
            printItem();
        }
        else {
            errorFetch();
        }

    }

    catch (e) {
        console.log(e);
    }
}

// Show Item
async function printItem() {

    const box_result = document.getElementById('result');

    final_result.data.forEach((item) => {
        const new_element = document.createElement('div');
        new_element.id = `file-${item.id}`;
        new_element.className = 'container-item';
        new_element.innerHTML = `
            <div class="container-item-default">
                <div id="image-${item.id}" class="container-image"><img src="${item.thumbnail_url}" onclick="zoom(this)"></div>
                <div class="container-info">
                    <span id="title-${item.id}" class="title">${item.filename}</span>
                    <div class="container-button">
                        <div id="container-download-${item.id}" class="container-download-button">
                            <button id="get-download-${item.id}" type="button" class="download-button">Download ${item.size}</button>
                        </div>
                        <div class="container-stream-button-valid">
                            <button id="stream-${item.id}" type="button" class="stream-button"><i class="fa-solid fa-play"></i></button>
                        </div>
                    </div>
                </div>
            </div>
            <div id="video-box-${item.id}" class="container-item-expand false">
            </div>`;
        box_result.appendChild(new_element);

        const downloadButton = new_element.querySelector(`#get-download-${item.id}`);
        downloadButton.addEventListener('click', () => {
            startDownload(item.id);
        });

        const streamButton = new_element.querySelector(`#stream-${item.id}`);
        streamButton.addEventListener('click', () => {
            startStream(item.id);
        });
    });
}

// Download
async function startDownload(id) {

    const specific_file = final_result.data.find(item => item.id === id);
    const video_url = `${api}/proxy?url=${specific_file.video_url}`;

    const a = document.createElement('a');
    const uniqueId = `download-link-${id}`;

    a.id = uniqueId;
    a.href = video_url;
    a.target = '_blank';
    a.rel = 'noopener noreferrer';
    a.style.display = 'none';
    document.body.appendChild(a);

    a.click();
    document.getElementById(uniqueId).remove();
}

// Stream
async function startStream(id) {

    const stream_box = document.getElementById(`stream-video`);
    loading3(`stream-${id}`, true);

    const specific_file = final_result.data.find(item => item.id === id);
    stream_box.className = 'stream-video-section';
    stream_box.innerHTML = '';
    stream_box.innerHTML = `
        <video controls>
            <source id="stream-video-${id}" src="${api}/proxy?url=${specific_file.video_url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>`;
    loading3(`stream-${id}`, false);
}