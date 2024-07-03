import React from 'react';
import styled from 'styled-components';

const SidebarContainer = styled.aside`
  background-color: #f7f7f7;
  padding: 1rem;
  width: 200px;
  position: fixed;
  height: 100%;
`;

const Sidebar = () => (
  <SidebarContainer>
    <h2>Categories</h2>
    <ul>
      <li><a href="/category/men">Men</a></li>
      <li><a href="/category/women">Women</a></li>
    </ul>
  </SidebarContainer>
);

export default Sidebar;
