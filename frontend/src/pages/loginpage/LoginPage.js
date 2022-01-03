import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { Form, Button, Row, Col } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import Loader from '../../components/loader/Loader'
import Message from '../../components/message/Message'
import { login } from '../../actions/userActions'

const LoginPage = () => {
  const [ email, setEmail ] = useState('')
  const [ password, setPassword ] = useState('')

  return (
    <div>
      Login Page
    </div>
  )
}

export default LoginPage