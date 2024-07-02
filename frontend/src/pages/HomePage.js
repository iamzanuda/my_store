import React from 'react';
import { Grid, Container } from '@mui/material';
import Sidebar from '../components/Sidebar';
import ProductCard from '../components/ProductCard';

const products = [
  { id: 1, name: 'Product 1', price: '$100', image: '/path/to/image1.jpg' },
  { id: 2, name: 'Product 2', price: '$150', image: '/path/to/image2.jpg' },
  // Add more products as needed
];

function HomePage() {
  return (
    <Container>
      <Grid container spacing={2}>
        <Grid item xs={3}>
          <Sidebar />
        </Grid>
        <Grid item xs={9}>
          <Grid container spacing={2}>
            {products.map((product) => (
              <Grid item xs={6} key={product.id}>
                <ProductCard product={product} />
              </Grid>
            ))}
          </Grid>
        </Grid>
      </Grid>
    </Container>
  );
}

export default HomePage;
