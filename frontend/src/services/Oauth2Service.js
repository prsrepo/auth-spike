import http from "../http-common"

class Oauth2Service {
    getAuthURL(data) {
        return http.post("/oauth2/url", data);
    }
}

export default new Oauth2Service();

