# Alien Thrift Store
Ecommerce website for alien goods using React, TypeScript, Django and PostGres

from root
env\scripts\activate

from backend to start server
python manage.py runserver
http://127.0.0.1:8000/api/

front end
npm start
localhost:3000

django admin user brian (ususal no upper no symbol) brian@email.com///pass

https://www.google.com/search?q=scifi+parts&tbm=isch&ved=2ahUKEwj4x73civj0AhUvAzQIHeUcD0wQ2-cCegQIABAA&oq=scifi+parts&gs_lcp=CgNpbWcQAzIFCAAQgAQ6BwgjEO8DECc6CAgAEIAEELEDOggIABCxAxCDAToLCAAQgAQQsQMQgwE6BAgAEEM6BggAEAoQGFDHBFimKmCUK2gAcAB4AIABWIgB1AaSAQIxMpgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=tXTDYbiZAq-G0PEP5bm84AQ&bih=730&biw=1536&rlz=1C1MSNA_enUS667US667&hl=en

https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.pond5.com%2Fsci-fi-engine-part-3d-091023237_iconl.jpeg&imgrefurl=https%3A%2F%2Fwww.pond5.com%2F3d-models%2Fitem%2F91023237-sci-fi-engine-part&tbnid=nZsDBsT_sFjrOM&vet=12ahUKEwiju6eAi_j0AhVAHzQIHX41CuwQxiAoAHoECAAQEQ..i&docid=vwrESgKFjt_2GM&w=360&h=360&itg=1&q=scifi%20parts&hl=en&ved=2ahUKEwiju6eAi_j0AhVAHzQIHX41CuwQxiAoAHoECAAQEQ#imgrc=6-h1NBh9gVEG8M&imgdii=nnlP7EegUeHG1M

do cartscreen 28 again

Redux:
constants are variables with the action names
  export const USER_LOGOUT = 'USER_LOGOUT'
The reducer imports those constants
The reducer functions are waiting for part of the state object and an action
The reducer returns the state, loading, or error payloads

Then the store inports that reducer function and registers it to the store
  registering a state means adding it to be used

On action page, import constants
  sometimes, actions are functions that take in a param and header, then
  they make a request and dispatch data or errors

Dispatch sends things to and from actions. Such as form data payloads
An action can be like 'saveshippingaddress' which dispatches a action constant 'cart_save_shipping_address' and gets a payload. then in the actions we dispatch(setShippingAddress(the object data)) and it gets sent back.

action function gets called. dispatches a code with a payload. the data goes to the constant in the reducer we trigger that reducer, take the new data and set the new value of the state