function includeInnerHTML() {
  var z, i, elmnt, file, xhttp;
  /*loop through a collection of all HTML elements:*/
  z = document.getElementsByTagName('*');
  for (i = 0; i < z.length; i++) {
    elmnt = z[i];
    /*search for elements with a certain atrribute:*/
    file = elmnt.getAttribute('inner-html');
    if (file) {
      /*make an HTTP request using the attribute value as the file name:*/
      xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function () {
        if (this.readyState == 4) {
          if (this.status == 200) {
            elmnt.innerHTML = this.responseText;
          }
          if (this.status == 404) {
            elmnt.innerHTML = 'Page not found.';
          }
          /*remove the attribute, and call this function once more:*/
          elmnt.removeAttribute('inner-html');
          includeInnerHTML();
        }
      };
      xhttp.open('GET', file, true);
      xhttp.send();
      /*exit the function:*/
      return;
    }
  }
}

function includeOuterHTML() {
  var z, i, elmnt, file, xhttp;
  /*loop through a collection of all HTML elements:*/
  z = document.getElementsByTagName('*');
  for (i = 0; i < z.length; i++) {
    elmnt = z[i];
    /*search for elements with a certain atrribute:*/
    file = elmnt.getAttribute('outer-html');
    if (file) {
      /*make an HTTP request using the attribute value as the file name:*/
      xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function () {
        if (this.readyState == 4) {
          if (this.status == 200) {
            elmnt.outerHTML = this.responseText;
          }
          if (this.status == 404) {
            elmnt.outerHTML = 'Page not found.';
          }
          /*remove the attribute, and call this function once more:*/
          elmnt.removeAttribute('outer-html');
          includeOuterHTML();
        }
      };
      xhttp.open('GET', file, true);
      xhttp.send();
      /*exit the function:*/
      return;
    }
  }
}

function includeHeadHTML(file) {
  var elmnt, file, xhttp;
  /*Get the head element:*/
  elmnt = document.head;

  /*check if the file argument was passed:*/
  if (file) {
    /*make an HTTP request using the attribute value as the file name:*/
    xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
      if (this.readyState == 4) {
        if (this.status == 200) {
          elmnt.innerHTML = this.responseText;
        }
        if (this.status == 404) {
          elmnt.innerHTML = 'Page not found.';
        }
        /*call this function once more:*/
        includeHeadHTML();
      }
    };
    xhttp.open('GET', file, true);
    xhttp.send();
    /*exit the function:*/
    return;
  }
}
