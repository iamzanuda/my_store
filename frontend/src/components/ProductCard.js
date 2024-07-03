import React from 'react';
import styled from 'styled-components';

const Card = styled.div`
  border: 1px solid #ddd;
  margin: 1rem;
  padding: 1rem;
  width: calc(50% - 2rem);
  display: inline-block;
  vertical-align: top;
`;

const ProductCard = ({ product }) => (
  <Card>
    <img src={product.image} alt={product.name} style={{ width: '100%' }} />
    <h3>{product.name}</h3>
    <p>{product.price}</p>
    <button>Add to Cart</button>
  </Card>
);

export default ProductCard;
