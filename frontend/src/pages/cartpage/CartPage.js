import React, { useEffect } from 'react'
import { Link, useParams, useNavigate, useLocation } from "react-router-dom";
import { useDispatch, useSelector  } from 'react-redux'
import { Row, Col, ListGroup, Image, Form, Button, Card} from 'react-bootstrap'
import { Message } from '../../components/message/Message'
import { addToCart } from '../../actions/cartActions'


const CartPage = () => {
  // react router
  const { id } = useParams()
  const location = useLocation()
  const qty = location.search ? Number(location.search.split('=')[1]) : 1
  
  const dispatch = useDispatch()

  const cart = useSelector(state => state.cart)
  const { cartItems } = cart
  console.log('cartItems: ', cartItems)

  useEffect(() => {
    if (id) {
      dispatch(addToCart(id, qty))
    }
  }, [dispatch, id, qty])

  return (
    <div>
      Cart
    </div>
  )
}

export default CartPage