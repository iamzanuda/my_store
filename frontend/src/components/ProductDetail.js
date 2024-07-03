import React from 'react';
import styled from 'styled-components';

const DetailContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const ProductDetail = ({ product }) => (
  <DetailContainer>
    <img src={product.image} alt={product.name} style={{ width: '50%' }} />
    <h2>{product.name}</h2>
    <p>{product.description}</p>
    <p>{product.price}</p>
    <button>Add to Favorites</button>
    <button>Add to Cart</button>
  </DetailContainer>
);

export default ProductDetail;
