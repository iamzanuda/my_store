import React from 'react';
import { useParams } from 'react-router-dom';
import { Container, Grid, Typography, Button, CardMedia, CardContent, Card } from '@mui/material';

const product = {
  id: 1,
  name: 'Product 1',
  description: 'This is a detailed description of Product 1.',
  price: '$100',
  image: '/path/to/image1.jpg',
  rating: 4.5,
  reviews: [
    'Great product!',
    'Really liked it.',
    // Add more reviews as needed
  ],
};

function ProductPage() {
  const { id } = useParams();

  return (
    <Container>
      <Grid container spacing={2}>
        <Grid item xs={6}>
          <CardMedia
            component="img"
            height="500"
            image={product.image}
            alt={product.name}
          />
        </Grid>
        <Grid item xs={6}>
          <CardContent>
            <Typography variant="h4">{product.name}</Typography>
            <Typography variant="body1" color="text.secondary">{product.description}</Typography>
            <Typography variant="h5" sx={{ marginTop: '16px' }}>{product.price}</Typography>
            <Typography variant="body1" sx={{ marginTop: '16px' }}>Rating: {product.rating}</Typography>
            <Typography variant="body1" sx={{ marginTop: '16px' }}>Reviews:</Typography>
            {product.reviews.map((review, index) => (
              <Typography key={index} variant="body2" color="text.secondary">- {review}</Typography>
            ))}
            <Button variant="contained" color="secondary" sx={{ marginTop: '16px' }}>Add to Cart</Button>
            <Button variant="outlined" color="secondary" sx={{ marginTop: '16px', marginLeft: '8px' }}>Add to Favorites</Button>
          </CardContent>
        </Grid>
      </Grid>
    </Container>
  );
}

export default ProductPage;
