import React from 'react';
import styled from 'styled-components';

const HeaderContainer = styled.header`
  background-color: #333;
  color: #fff;
  padding: 1rem;
`;

const Header = () => (
  <HeaderContainer>
    <h1>Clothing Store</h1>
    <nav>
      <a href="/login">Login</a> | <a href="/register">Register</a>
    </nav>
  </HeaderContainer>
);

export default Header;
