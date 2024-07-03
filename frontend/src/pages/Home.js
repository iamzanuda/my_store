import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ProductCard from '../components/ProductCard';
import Sidebar from '../components/Sidebar';
import styled from 'styled-components';

const MainContent = styled.div`
  margin-left: 220px;
  padding: 1rem;
`;

const Home = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get('/api/products').then(response => {
      setProducts(response.data);
    });
  }, []);

  return (
    <div>
      <Sidebar />
      <MainContent>
        {products.map(product => (
          <ProductCard key={product.id} product={product} />
        ))}
      </MainContent>
    </div>
  );
};

export default Home;
