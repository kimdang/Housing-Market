import axios from 'axios'
import { async } from 'q';

const FETCH_FIGURE = 'FETCH_FIGURE'

// end point
// const URL = 'http://localhost:8000/housing'
const URL = 'http://54.244.202.224:8000/housing'

export function fetchFigure(city,state) {
    return async dispatch => {
        const req = await axios.get(`${URL}/${city}/${state}/`)
        return dispatch({
            type: FETCH_FIGURE,
            payload: req.data
        })
    }
}