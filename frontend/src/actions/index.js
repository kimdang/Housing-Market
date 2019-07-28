import axios from 'axios'
import { async } from 'q';

const FETCH_FIGURE = 'FETCH_FIGURE'
const INPUT_ERROR = 'in'
// end point
//const URL = 'http://localhost:8000/housing'
const URL = 'http://35.166.12.129:8000/housing'

const stateList = { "Alaska" : "AK", "Alabama" : "AL", "Arkansas" : "AR", "American Samoa" : "AS", "Arizona" : "AZ", "California" : "CA", "Colorado" : "CO", "Connecticut" : "CT", "District of Columbia" : "DC", "Delaware" : "DE", "Florida" : "FL", "Georgia" : "GA", "Guam" : "GU", "Hawaii" : "HI", "Iowa" : "IA", "Idaho" : "ID", "Illinois" : "IL", "Indiana" : "IN", "Kansas" : "KS", "Kentucky" : "KY", "Louisiana" : "LA", "Massachusetts" : "MA", "Maryland" : "MD", "Maine" : "ME", "Michigan" : "MI", "Minnesota" : "MN", "Missouri" : "MO", "Mississippi" : "MS", "Montana" : "MT", "North Carolina" : "NC", "North Dakota" : "ND", "Nebraska" : "NE", "New Hampshire" : "NH", "New Jersey" : "NJ", "New Mexico" : "NM", "Nevada" : "NV", "New York" : "NY", "Ohio" : "OH", "Oklahoma" : "OK", "Oregon" : "OR", "Pennsylvania" : "PA", "Puerto Rico" : "PR", "Rhode Island" : "RI", "South Carolina" : "SC", "South Dakota" : "SD", "Tennessee" : "TN", "Texas" : "TX", "Utah" : "UT", "Virginia" : "VA", "Virgin Islands" : "VI", "Vermont" : "VT", "Washington" : "WA", "Wisconsin" : "WI", "West Virginia" : "WV", "Wyoming" : "WY" }

export function fetchFigure(city,state) {
    city = city.replace(' ', '_')
    if (state.trim().length > 2) {
        state = stateList[state]
    }
    if (state === undefined) {
        return dispatch => {
            return dispatch({
                type: INPUT_ERROR,
                payload: 'You enter wrong information'
            })
        }
    }
    return async dispatch => {
        const req = await axios.get(`${URL}/${state}/${city}/`)
        return dispatch({
            type: FETCH_FIGURE,
            payload: req.data
        })
    }
}