const name = document.getElementById('name')
const password = document.getElementById('password')
const birthday = document.getElementById('birthday')
const email = document.getElementById('email')
const phone = document.getElementById('phone')
const form = document.getElementById('form')
const errorName = document.getElementById('error-name')
const errorPass = document.getElementById('error-pass')
const errorPhone = document.getElementById('error-phone')
const errorMail = document.getElementById('error-mail')

form.addEventListener('submit', (e) =>{
    let messagename = []
    let messagepass = []
    let messagephone = []
    let messagemail = []
    let regname=/^[a-zA-Z]{1,6}$/
    let regpass=/^[a-zA-Z0-9\._]:{6,}$/
    let regmail=/^[a-zA-Z0-9_.]{4,15}@[a-z]*\.com$/
    if (!regname.test(name.value)){
        messagename.push('Invalid Name')
    }
    if (!regpass.test(password.value)){
        messagepass.push('Invalid Password')
    }
    if (phone.value === '' || phone.value ===null){
        messagephone.push('Phone Number is required')
    }
    if (phone.value.length > 0 && phone.value.length != 10 ){
            messagephone.push('Phone Number must be 10 digits')
    }
    if(email.value.length > 0 && !regmail.test(email.value)){
        messagemail.push('Email is Invalid')
        }
    if (messagename.length > 0){
        e.preventDefault()
        errorName.innerText = messagename.join(', ')
    }
    if (messagepass.length > 0){
        e.preventDefault()
        errorPass.innerText = messagepass.join(', ')
    }
    if (messagephone.length > 0){
        e.preventDefault()
        errorPhone.innerText = messagephone.join(', ')
    }
    if (messagemail.length > 0){
        e.preventDefault()
        errorMail.innerText = messagemail.join(', ')
    }
    
})