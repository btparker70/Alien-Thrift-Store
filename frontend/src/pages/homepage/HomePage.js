import React, { useState, useEffect } from 'react'
import { Row, Col,  } from 'react-bootstrap'
import products from '../../products'
import Product from '../../components/product/Product'
import axios from 'axios'


const HomePage = () => {
  const [ products, setProducts ] = useState([]);

  useEffect(() => {

    async function fetProducts() {

      const { data } = await axios.get('/api/products/');
    setProducts(data)
    }

    fetProducts();

  }, [])

  return (
    <div>
      <h1>Latest Products</h1>
      <Row>
        {products.map((product, index) => (
          <Col key={product._id} sm={12} md={6} lg={4} xl={3}>
            <Product product={product}/>
          </Col>
        ))}
      </Row>
    </div>
  )
}

export default HomePage
