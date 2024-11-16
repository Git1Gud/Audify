import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import LandingPage from "./components/pages/Landingpage";
import CensorAudio from "./components/pages/CensorPage";

const router = createBrowserRouter([
  {
    path: "/",
    element: <LandingPage />
  },
   {
    path: "/censor",
    element: <CensorAudio />
  },
]);

export default function App() {
  return (
    <RouterProvider router={router} />
  );
}
