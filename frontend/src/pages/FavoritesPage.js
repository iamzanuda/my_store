import React from 'react';
import { Container, Typography, Grid } from '@mui/material';
import ProductCard from '../components/ProductCard';

// Sample favorite products data
const favoriteProducts = [
  { id: 1, name: 'Product 1', price: '$100', image: '/path/to/image1.jpg' },
  { id: 2, name: 'Product 2', price: '$150', image: '/path/to/image2.jpg' },
  // Add more favorite products as needed
];

function FavoritesPage() {
  return (
    <Container>
      <Typography variant="h4" sx={{ marginBottom: '16px' }}>Favorites</Typography>
      <Grid container spacing={2}>
        {favoriteProducts.map((product) => (
          <Grid item xs={6} key={product.id}>
            <ProductCard product={product} />
          </Grid>
        ))}
      </Grid>
    </Container>
  );
}

export default FavoritesPage;
