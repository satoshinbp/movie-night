import Watchlist from './pages/Watchlist'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

export default function App() {
  const router = createBrowserRouter([
    {
      path: '/',
      element: <Watchlist />,
    },
  ])

  return <RouterProvider router={router} />
}
