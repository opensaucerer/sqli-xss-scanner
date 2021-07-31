const body = document.querySelector('body');
const section = document.querySelector('section');

const loader = '<div id="loader_div" class="loader_div"></div>';

const scan = document.querySelector('#submit');
const form = document.querySelector('form');
const input = document.querySelector('#url');

form.onsubmit = async function () {
  //   body.innerHTML = loader;
  url = input.value;

  section.style.display = 'none';
  body.innerHTML += loader;

  location.href = `u_report?url=${url}`;

  //   response = await fetch(`report?url=${url}`);
};
