let languages = document.querySelectorAll("button.language");
let filename = location.pathname.split("/").pop();
if (!filename) filename = 'index.html';

console.log(filename);

languages.forEach(function (value, index) {
    languages[index].addEventListener('click', function () {
        switchLanguage(this.dataset.lang);
    });
});

let xhttp = new XMLHttpRequest();
xhttp.onload = function () {
    if (this.status === 200) {
        processLangDocument(JSON.parse(this.responseText)[filename]);
    }
};

function switchLanguage(language) {
    document.cookie = "lang=" + language + "; path=/; SameSite=Lax;"
    xhttp.open("GET", "assets/json/" + language + ".json", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send();
}

function processLangDocument(langDict) {
    let tags = document.querySelectorAll('[data-langkey]');

    tags.forEach(function (value) {
        let key = value.dataset.langkey;
        let translation = langDict[key];
        if (langDict && translation) {
            value.innerHTML = translation;
        }
    });

    let imgTags = document.querySelectorAll('img');
    imgTags.forEach(function (value) {
        if (value.hasAttribute("alt")) {
            let key = value.dataset.langkey;
            let translation = langDict["alts"][key];
            if (translation) {
                value.setAttribute("alt", translation);
            }
        }
    });
    let aTags = document.querySelectorAll('a');
    aTags.forEach(function (value) {
        if (value.hasAttribute("title")) {
            let key = value.dataset.langkey;
            let translation = langDict["titles"][key];
            if (translation) {
                value.setAttribute("title", translation);
            }
        }
    });

    let buttons = document.querySelectorAll('[data-lang]');
    buttons.forEach(function (value) {
        value.classList.remove("active");
        value.classList.remove("active_default-cursor")
    });
    let curLang = getCookie("lang");
    let b = document.querySelector('[data-lang=' + curLang + ']');
    b.classList.add("active");
    b.classList.add("active_default-cursor")
}

function getCookie(cname) {
    let name = cname + "=";
    let ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
         let c = ca[i];
         while (c.charAt(0) === ' ') {
            c = c.substring(1);
         }
         if (c.indexOf(name) === 0) {
            return c.substring(name.length, c.length);
         }
    }
    return "";
}

function loadLanguage() {
    let curLang = getCookie("lang");
    if (curLang !== "") {
        switchLanguage(curLang);
    }
}

loadLanguage();

/******************************************************/
let links = document.querySelectorAll("a.nav-link, a.up, a.to-next-page, a.to-previous-page, a.to-inx-page");
let x = window.matchMedia("(max-width: 974px)");
let flag = true;

function addPostfix(value) {
    let ref = (value.classList.contains("up"))? filename: value.getAttribute("href");
    let postfix = ref.split(".")[0];
    if (postfix.localeCompare("index") === 0) {
        postfix = "main";
    }
    value.setAttribute("href", ref + "#" + postfix);
}

function removePostfix(value) {
    if (value.classList.contains("up")) {
        value.setAttribute("href", "#");
    }
    else {
        let ref = value.getAttribute("href");
        value.setAttribute("href", ref.split("#")[0]);
    }
}

function myFunction(x) {
    if (x.matches && flag) {
        flag = false;
        links.forEach(addPostfix);
    } else if (!x.matches) {
        flag = true;
        links.forEach(removePostfix);
    }
}

x.addListener(myFunction);
myFunction(x);