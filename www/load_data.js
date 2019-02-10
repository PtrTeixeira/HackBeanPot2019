const post = (url, postBody) => fetch(url, {
  method: 'POST',
  body: JSON.stringify(postBody),
  headers: {
    'Content-Type': 'application/json'
  }
})

const removeChildren = (node) => {
  while (node.firstChild) {
    node.removeChild(node.firstChild)
  }
}

const buildDisplayElement = (caption, url, isVideo = false) => {
  if (isVideo) {
    const imageElement = document.createElement('video')
    imageElement.src = url
    imageElement.classList.add("card-img-top")

    return imageElement
  } else {
    const imageElement = document.createElement('img')
    imageElement.src = url
    imageElement.alt = caption
    imageElement.classList.add("card-img-top")

    return imageElement
  }
};

const buildElementHtml = ({ caption, image, video }) => {
  const imageElement = buildDisplayElement(caption, image, video)

  const captionElement = document.createElement("p")
  captionElement.innerText = caption
  captionElement.setAttribute('aria-hidden', true)
  captionElement.classList.add("card-text")

  const msg = new SpeechSynthesisUtterance(caption);

  const readButton = document.createElement("button")
  readButton.textContent = "Read Content"
  readButton.onclick = () => {
    window.speechSynthesis.speak(msg)
  }

  const captionWrapperElement = document.createElement("div")
  captionWrapperElement.classList.add("card-body")
  captionWrapperElement.appendChild(captionElement)
  captionWrapperElement.appendChild(readButton)

  const wrapperElement = document.createElement("div")
  wrapperElement.classList.add("card")
  wrapperElement.classList.add("mb-3")

  wrapperElement.appendChild(imageElement)
  wrapperElement.appendChild(captionWrapperElement)

  return wrapperElement
}

const clickHandler = () => {
  const usernames = document
    .getElementById('users-field')
    .value
    .split(',')
    .map(name => name.trim())

  const postBody = {
    imageCount: 5,
    usernames
  }

  post("http://localhost:5000/api/load", postBody)
    .then(response => response.json())
    .then(data => {
      const targetElement = document.getElementById('output-text')
      removeChildren(targetElement)

      data.forEach(imageData => {
        const childElement = buildElementHtml(imageData)
        targetElement.appendChild(childElement)
      })
    })

  return false;
}

document.getElementById('load-data').onclick = clickHandler
